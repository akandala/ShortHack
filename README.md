# Prospect predict
We are planning to implement a model that predicts prospect converted to Leased or Unqualified. this will help the marketing people and as well to the property owners to see in depth what features he opted, for example if the price range between so and so are mostly predicted as active lease etc,... 

## Features:  
  ### Functional: 
        1) Lead form, where consumer provide his basic information as we currently have in OneSite.     
        2) Build complete workflow for creating Model, API to predict based on created model    
        2) Notification for Site leasing agent. 
        3) Dashboard for verifying lease status with their key feature

  ### Non-functional:
        1) Docorizing the application
        2) Continuous Integration using GitHub actions

## Tech: 

 ### Backend: 
    - we will build on these open-source framework / libraries -  

    [Python]: For general purpose coding 

    Python Flask: For building API 

    [SqlALchemy]: performing ORM operations. 

    [MySQL]: Database 

    Kafka: for sending messages. 

    MLFlow: managing the end-to-end machine learning lifecycle. 

    Docker: to dockize application for easy installations. 

 ### Frontend:  
   Angular: UI/UX actions / events on HTML documents, DOM transformation and accessing resources.  

   Bootstrap: Great UI experience look and feel.  

## Installation: 
    1) git clone https://tfs.realpage.com/tfs/Realpage/ShortHack/_git/BeABeginner
    2) Navigate to git repo
    3) "docker build -t prospectpredictor ."
    4) docker compose build
    5) docker-compose up -d 
    6) docker-compose logs - view api running information
    7) verify health using http://localhost/healthcheck
    8) Curl info below: 
        curl --location --request POST 'http://localhost/Predict' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "BrokenLease": 0,
        "County": "UA",
        "CriminalQuestion": 0,
        "DOB": "01/01/2002",
        "Evicted": 0,
        "Gender": "M",
        "IsInternationalApplicant": 0,
        "MaritalStatus": "M",
        "PrefCommunicationType": "",
        "ResidentDesignation": "",
        "SuedForDamage": 0,
        "SuedForRent": 0,
        "city": "Dadfllas",
        "countryCode": "UA",
        "gcardId": 37,
        "gcardOccupantCount": 2,
        "gcardPreferedFloorplanGroupId": "2Bed",
        "jobTypeID": "10",
        "phoneType1": "M",
        "phoneType2": "J",
        "relCode": "H",
        "rentOwnFlag": "N",
        "state": "Test",
        "status": 1,
        "trfsrcName": "internet",
        "zip": "654321"
    }
    