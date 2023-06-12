import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http'


@Component({
  selector: 'app-applicant-form',
  templateUrl: './applicant-form.component.html',
  styleUrls: ['./applicant-form.component.css'],
})
export class ApplicantFormComponent {

  form: FormGroup = new FormGroup({});

  constructor(private fb: FormBuilder,private http: HttpClient) { }
  ngOnInit(): void {
    this.form = this.fb.group({
      firstName: [null],
      lastName: [null],
      dob : [null],
      brokenLease:[null],
      CriminalQuestion:[null],
      IsInternationalApplicant:[null],
      SuedForDamage:[null],
      Evicted:[null],
      SuedForRent:[null],
      city:[null],
      countryCode:[null],
      state:[null],
      County:[null],
      zip:[null],
      phoneType1:[null],
      phoneType2:[null],
      trfsrcName:[null],
      gcardOccupantCount:[null],
      Gender:[null],
      rentOwnFlag:[null]
    });
  }

  saveDetails(form: any) {
    //alert('SUCCESS!! :-)\n\n' + JSON.stringify(form.value, null, 4));
    const headers = { 'Authorization': 'Bearer my-token', 'My-Custom-Header': 'foobar' };
        const body = {
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
        this.http.post<any>('http://10.13.115.191:5000/Predict', body, {  }).subscribe(data => {
            console.log(data)
            if(data.Predict == 1){
              alert('SUCCESS!! :-)\n\n');
            }else{
              alert('Fail!! :-)\n\n');
            }
        });
  }
}