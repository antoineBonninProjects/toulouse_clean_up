import { Component } from '@angular/core';
import { OnInit } from '@angular/core';

import { DataLatestForOneService } from "./data-latest-forone.service";

@Component({
	selector: 'data_latest_forone',
  	templateUrl: './data-latest-forone.component.html',
	providers: [DataLatestForOneService],
})
export class DataLatestForOneComponent implements OnInit{
	data;

	constructor (private _dataService: DataLatestForOneService) {
	}

	ngOnInit():any {
		this._dataService.getLatestWeight().subscribe(
				data => this.data = JSON.parse(JSON.stringify(data)).weight,
				error => alert(error),
				() => console.log("Finished !")
			);

		this._dataService.listen('weight_update').subscribe(res => {
      		this.data  = res.weight;
		});
	}
} 