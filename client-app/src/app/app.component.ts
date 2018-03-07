import { Component } from '@angular/core';

import {ContactComponent} from "./contact/contact.component";
import {DataComponent} from "./data/data.component";


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'my_SigFox_project';
}
