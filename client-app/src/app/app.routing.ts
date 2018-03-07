import { RouterModule, Routes } from '@angular/router';
import { ModuleWithProviders } from '@angular/core';

import { HomeComponent } from "./home/home.component";

import { DataComponent } from "./data/data.component";
import { DataLatestForallComponent } from "./data/data-latest/data-latest-forall/data-latest-forall.component";
import { DataLatestForOneComponent } from "./data/data-latest/data-latest-forone/data-latest-forone.component";
import { DataMultipleForOneComponent } from "./data/data-multiple/data-multiple-forone/data-forone.component";

import { ContactComponent } from "./contact/contact.component";


const appRoutes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent},
  { path: 'contact', component: ContactComponent },
  { path: 'data', component: DataComponent,
	children: [
			    {
	              path: '',
	              component: DataLatestForallComponent
	            },
	            {
	              path: 'latest/forall',
	              component: DataLatestForallComponent
	            },
	            {
	              path: 'latest/1D1901',
	              component: DataLatestForOneComponent
	            },
	            {
	              path: 'forone',
	              component: DataMultipleForOneComponent
	            }
	          ]  
  }];

export const appRouting: ModuleWithProviders = RouterModule.forRoot(appRoutes);