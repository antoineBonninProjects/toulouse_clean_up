import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';
import { FormsModule } from '@angular/forms';

import { appRouting } from './app.routing';
 

import { AppComponent } from './app.component';

import { ContactComponent } from "./contact/contact.component";

import { DataComponent } from "./data/data.component";
import { DataLatestForOneComponent } from "./data/data-latest-forone.component";
import { DataLatestForallComponent } from "./data/data-latest-forall.component";




@NgModule({
  declarations: [
    AppComponent,
    ContactComponent, 
    DataComponent,
    DataLatestForallComponent,
    DataLatestForOneComponent
  ],
  imports: [
    BrowserModule,
    HttpModule,
    appRouting
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
