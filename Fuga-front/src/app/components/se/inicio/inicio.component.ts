import { Component, OnInit } from '@angular/core';
import { Data } from '@angular/router';
import { DataService } from 'src/app/services/data.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-inicio',
  templateUrl: './inicio.component.html',
  styleUrls: ['./inicio.component.css']
})
export class InicioComponent implements OnInit {
  message: string = '';
  question: string = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!'
  response: string = '';
  opciones: any[] = [
    {name: 'pvc'},
    {name: 'plomo'},
    {name: 'cobre'},
  ];
  typeForm: number = 1;
  Form: any = 0;
  Final: string = '';
  siguiente: number = 0;
  displayBasic: boolean = false;
  resultado: string = '';
  constructor(
    private _dataService: DataService,
    private rutaActiva: ActivatedRoute
  ) { 
  }

  ngOnInit(): void {
    this.Form = this.rutaActiva.snapshot.params['question'];
    this._dataService.getInicio({'tipo': this.Form}).subscribe(
      (result:any)=>{
        this.typeForm = result?.tipo;
        this.question = result?.texto;
        this.siguiente = result?.siguiente;
        console.log(result);
      }
    );
  }
  nextStep(){
    this.Final += this.response +';' 
    this._dataService.nextStep({'tipo': this.Form}).subscribe(
      (result:any)=>{
        this.typeForm = result?.tipo;
        this.question = result?.texto;
        this.siguiente = result?.siguiente;
        console.log(result);
      }
    );
  }
  enviarRespuesta(){
    this.Final += this.response;
    this._dataService.getResult({'answer': this.Final, 'tipo': this.Form}).subscribe(
      (result:any)=>{
        this.resultado = 'la casa cuenta con indicios de una fuga de agua'
        this.displayBasic = true;
      }
    );
  }
}
