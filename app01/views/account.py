from django.shortcuts import render, HttpResponse, redirect
from django import forms
from app01.utils.bootstrap import BootstrapForm
from app01.utils.encrypt import md5
from app01 import models
from app01.utils.code import check_code
from io import BytesIO




class LoginForm(BootstrapForm):
    username = forms.CharField(
        label="username",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )
    code = forms.CharField(
        label="code",
        widget=forms.TextInput,
        required=True
    )



    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)




def login(request):
    """Login Page"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # if check info as valid
        # print(form.cleaned_data)


        # Check the verification code
        user_input_code = form.cleaned_data.pop("code")
        real_code = request.session.get("image_code", "")
        # print(real_code)
        if real_code.upper() != user_input_code.upper():
            form.add_error("code", "wrong verification code")
            return render(request, "login.html", {"form": form})


        # Check md5 password in the database, get User object
        # admin_object = models.Admin.objects.filter(username=form.cleaned_data['username'],password=form.cleaned_data['password']).first()
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "username or password error")
            return render(request, "login.html", {"form": form})

        # When username and password are correct
        # Generate random string as a cookie and put it inside user's browser, and save a copy to the session
        request.session["info"] = {"id": admin_object.id, "name": admin_object.username}
        # If login successfully, the session can be reserved for 7 days
        request.session.set_expiry(60 * 60 * 24 * 7)

        return redirect("/admin/list/")

    return render(request, "login.html", {"form": form})




def logout(request):
    """User Logout"""
    # Clear the cookie sent to the browser
    request.session.clear()
    return redirect('/login/')




def image_code(request):
    """Generate random verification code"""
    # Apply pillow package and generate pictures
    img, code_string = check_code()

    # Put the code info to the session in order to get it later
    request.session['image_code'] = code_string
    # Make the session expire after 60 secs
    request.session.set_expiry(60)



    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())










