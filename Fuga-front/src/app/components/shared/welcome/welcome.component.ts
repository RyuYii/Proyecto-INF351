import { Component, OnInit } from '@angular/core';
import { DataService } from 'src/app/services/data.service';

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css']
})
export class WelcomeComponent implements OnInit {

  questions: any[] = [];
  constructor(
    private _dataService: DataService
  ) { }

  ngOnInit(): void {
    this._dataService.getQuestions().subscribe(
      (result: any) => {
        //console.log(result)
        this.questions = result;
      }
    )
  }

}
