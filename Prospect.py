class Prospect:
    
    def __init__(self,gcardId,relCode,phoneType1,phoneType2,city,state,zip,countryCode,jobTypeID,rentOwnFlag,DOB,Gender, CriminalQuestion,BrokenLease,Evicted,SuedForDamage,SuedForRent,MaritalStatus
                 ,ResidentDesignation,IsInternationalApplicant,PrefCommunicationType,County,status,trfsrcName,gcardPreferedFloorplanGroupId,gcardOccupantCount):

        self.gcardId = gcardId
        self.relCode = relCode
        self.phoneType1 = phoneType1
        self.phoneType2 = phoneType2
        self.city = city
        self.state = state
        self.zip = zip
        self.countryCode = countryCode
        self.jobTypeID =jobTypeID
        self.rentOwnFlag = rentOwnFlag
        self.DOB = DOB
        self.Gender = Gender
        self.CriminalQuestion = CriminalQuestion
        self.BrokenLease = BrokenLease
        self.Evicted = Evicted
        self.SuedForDamage = SuedForDamage
        self.SuedForRent = SuedForRent
        self.MaritalStatus = MaritalStatus
        self.ResidentDesignation = ResidentDesignation
        self.IsInternationalApplicant = IsInternationalApplicant
        self.PrefCommunicationType = PrefCommunicationType
        self.County = County
        self.status = status
        self.trfsrcName = trfsrcName
        self.gcardPreferedFloorplanGroupId = gcardPreferedFloorplanGroupId
        self.gcardOccupantCount = gcardOccupantCount
    
    def example():        
        return Prospect(0,'H','H','W','Dallas','Texas','654321','UA','10','N','01/01/2002','M', 0,0,0,0,0,'','',0,'','UA',1,'internet','2Bed',2)











 












