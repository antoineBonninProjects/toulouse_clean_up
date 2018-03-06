import { RouterModule, Routes } from '@angular/router';
import { ModuleWithProviders } from '@angular/core';

import { ContactComponent } from "./contact/contact.component";

import { DataComponent } from "./data/data.component";
import { DataLatestForallComponent } from "./data/data-latest-forall.component";
import { DataLatestForOneComponent } from "./data/data-latest-forone.component";


const appRoutes: Routes = [
  { path: '', redirectTo: 'data', pathMatch: 'full' },
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
	            }
	          ]  
  }];

export const appRouting: ModuleWithProviders = RouterModule.forRoot(appRoutes);