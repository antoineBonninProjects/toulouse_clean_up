import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';
import { FormsModule } from '@angular/forms';

import { appRouting } from './app.routing';
 

import { AppComponent } from "./app.component";

import { HomeComponent } from "./home/home.component";

import { DataComponent } from "./data/data.component";
import { DataLatestForOneComponent } from "./data/data-latest/data-latest-forone/data-latest-forone.component";
import { DataLatestForallComponent } from "./data/data-latest/data-latest-forall/data-latest-forall.component";
import { DataMultipleForOneComponent } from "./data/data-multiple/data-multiple-forone/data-forone.component";


import { ContactComponent } from "./contact/contact.component";



@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    DataComponent,
    DataLatestForallComponent,
    DataLatestForOneComponent,
    DataMultipleForOneComponent,
    ContactComponent
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
