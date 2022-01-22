import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL } from 'src/environments/environment';
@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(
    private http: HttpClient
  ) { }

  getInicio(cuestion: object){
    return this.http.post(`${API_URL}obtenerOpciones`, cuestion)
  }

  nextStep(answer: object){
    return this.http.post(`${API_URL}nextStep`, answer)
  }

  getQuestions(){
    return this.http.get(`${API_URL}/questions`)
  }

  getResult(answer: object){
    return this.http.post(`${API_URL}result`, answer)
  }
}
