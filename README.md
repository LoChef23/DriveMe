# DriveMe
Drive me is an application aimed to help users preparing exams or studying any kind of topic with some simple true/false Quizzes.
In our use case we choosed the driving license topic.

# Solution
Application has been developed using the REST architecture style and could be divided into 2 main parts:

1. authentication: done using JSON Web Token and consisting into 2 endpoints:

   a) POST request: [...]/registration
   
      Input sample:
      
      {
	       "username":"UserTest42",
	       "email": "fortytwo@email.com",
	       "password":"secretPsw42!"
      }
      
      Output sample:
      
      {
          "accessToken":     
          "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Nzg1MjAwOTEsIm5iZiI6MTU3ODUyMDA5MSwi
           anRpIjoiMWVjMGI1ZGEtMGVkZC00MDliLTg0ODQtZDYyYzQyZGJiNDg2IiwiZXhwIjoxNTc4NT
           IwOTkxLCJpZGVudGl0eSI6ImdpdWxpbzk4NzgwNyIsImZyZXNoIjpmYWxzZSwidHlw
           ZSI6ImFjY2VzcyJ9.yXbp3LsbXJO8Nh-KSMHVRgu1j4ZV_tk9lCc6oBlJIns"
       }
           
   b) POST request: [...]/login
   
      Input sample:
      
      {
	       "username":"UserTest42",
	       "password":"secretPsw42!"
      }
      
      Output sample:
      
      {
          "accessToken":     
          "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Nzg1MjAwOTEsIm5iZiI6MTU3ODUyMDA5MSwi
           anRpIjoiMWVjMGI1ZGEtMGVkZC00MDliLTg0ODQtZDYyYzQyZGJiNDg2IiwiZXhwIjoxNTc4NT
           IwOTkxLCJpZGVudGl0eSI6ImdpdWxpbzk4NzgwNyIsImZyZXNoIjpmYWxzZSwidHlw
           ZSI6ImFjY2VzcyJ9.yXbp3LsbXJO8Nh-KSMHVRgu1j4ZV_tk9lCc6oBlJIns"
      }
    
2. core part: after receiving the request and verifying the validity of the Token, answers with a random question retrieved from the      database. This part consists in 1 endpoint:
   
   c) GET request: [...]/question
   
      Input sample:
      
      only the Token should be specified in the Header of the request into the Authorization field
      
      Output sample:
      
      {
            "questionID": "745",
            "questionText": "Il segnale raffigurato preannuncia barriere di recinzione di un cantiere stradale",
            "questionAnswer": false,
            "questionImage": "passaggio_a_livello_con_barriere.gif"
      }
      
  
# Architecture
Application has been deployed on an AWS EC2 instance and uses the NoSQL database AWS Dynamo DB:








