# RHDEV-BE-2-flask


1) GET /

Get welcome message

Function used : hello()
Source: main.py

Parameters : None

Response : welcome message string

Example : ``` Welcome message! ```

2) GET /profiles/<int:id>/

Get name and all scores of a profile

Function used : getid(id)
Source: ProfilesAPI.py

Parameters : None

Response : JSON of status and profile

Example : ``` {"Status" : "Success", "Details" : {"name": "Nobel", "scores": [1, 2, 3, 4, 5]} } ```

3) POST /profiles/profiles

Create a new profile

Function used : postid()
Source: ProfilesAPI.py

Parameters : None

Response : JSON of status and details of new profile

Example : ``` {"Status" : "Success", "Details" : {"name": "Vina"}} ```

4) DELETE /profiles/<int:id>/

Delete a profile

Function used : deleteid(id)
Source: ProfilesAPI.py

Parameters : None

Response : JSON of status and details of deleted profile. If failed then json of status and message 'No such ID'

Example : ``` {"Status" : "Success", "Details" : {"name": "Nobel", "scores": [1, 2, 3, 4, 5]}} ``` or ```{"Status" : "Error", "Message" : "No such ID"}```

5) GET /profiles/<int:id>/score

Get all scores of a profile, above the min score and if min score not provided, return all scores

Function used : getabovemin(id)
Source: ProfilesAPI.py

Parameters : minScore

Response : JSON of status and details of scores. If failed then json of status and message 'No such ID'

Example : if minScore=3``` {"Status" : "Success", "Details" : [4, 5]}} ``` or ```{"Status" : "Error", "Message" : "No such ID"}``` or if minScore= ```{"Status" : "Success", "Details" : [1, 2 ,3, 4, 5]}}```

6) POST /auth/register

Stores a username and hashedPassword (given as hashed) and store it in a local array ('creds')

Function used : reg()
Source: AuthAPI.py

Parameters : 

username (Required) 
Username of user

passwordHash (Required)
Password of user

Response : JSON of message - registered and status. If failed then json of status and message 'No such ID'

Example : ```{"Message": "Registered","Status": "Success"}```


6) POST /auth/login

Checks if the provided information is valid and return a jwt token + success message

Function used : login()
Source: AuthAPI.py

Parameters : 

username (Required) 
Username of user

passwordHash (Required)
Password of user

Response : JWT token and status. 

Example : ```{"Status": "Success","token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOiJ2aW5hIiwicGFzc3dvcmRIYXNoIjoidGVzdDEyMyJ9.CHFN38N9mQ7Fu3If9ELcHaOdm0x7S6tctmF1crzoW64"}```



