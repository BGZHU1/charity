from rest_framework import serializers
from .models import  Profile
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect



class ProfileSerializer(serializers.ModelSerializer):
    first_name =serializers.CharField(max_length=100, required=True)
    last_name = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'}, required=True)
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'}, required=True)
    email = serializers.EmailField()

    '''
    if validated_data['password'] != validated_data['password2']:
        raise serializers.ValidationError("two passwords must be the same value")
    return validated_data['password']
    
    
    '''

    def validate(self, value, *args, **kwargs):
        if value['password'] != value['confirm_password']:

            raise serializers.ValidationError({
                'password': ['please enter same password twice']
            })

        if  Profile.objects.filter(username = value['email']).exists():

            raise serializers.ValidationError({
                'email': ['please enter a different email address']
            })

        return value

    def create(self, validated_data):
        user = Profile.objects.create(
            username = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name= validated_data['last_name'],
            charity_list='',
            number_hours=0
            )


        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = Profile
        # Tuple of serialized model fields (see link [2])
        fields = ('first_name', 'last_name', 'password', 'confirm_password', 'email')

'''
class Profile(User):
    class Meta:
        ordering = ["last_name"]

    charity_list = models.CharField(max_length=100, default='Volunteers_Home')
    number_hours = models.FloatField(default=0)
    objects = UserManager()
'''


'''
def register(request) :
    #return HttpResponse('homepage')
    #return render(request, 'homepage.html')
    #figure out how to create new user and authentication
    if request.method == 'POST':
        #need to validate form information here

        user_info = request.POST
        print(user_info)
        firstname = user_info['firstname']
        lastname = user_info['lastname']
        email = user_info['email_address']
        password = user_info['password']
        password2 = user_info['password2']
        #charity = user_info['charity_name']
        if password != password2 :
            template = loader.get_template('user_register.html')
            context = {
                'user_creation_failed' : 'please enter the same password twice'
            }
            return HttpResponse(template.render(context, request))

        charity = ''
        print(user_info)
        print('form', UserRegistrationForm(request.POST).is_valid())

        user = None
        try :

            #user = User.objects.create_user(username = email, password = password,  first_name = firstname, last_name = lastname)
            #user.save()
            #some how need to validate form
            if UserRegistrationForm(request.POST).is_valid():
                profile = models.Profile.objects.create(username = email, first_name = firstname, last_name = lastname, charity_list =charity, number_hours = 0)
                profile.set_password(password)
                #profile = models.Profile.objects.create(user=user, charity_list =charity, number_hours = 0, firstname = firstname, lastname = lastname)
                profile.save()

        except :
            template = loader.get_template('user_register.html')
            context = {
                'user_creation_failed' : 'the email already exists, please use an different email and try again'
            }
            return HttpResponse(template.render(context, request))


        #return render(request, "user_register.html", {"form": user_profile})


        return HttpResponseRedirect('/user/login/')
    else:
        profile = Profile()
        return render(request, "user_register.html", {"form": profile})


'''