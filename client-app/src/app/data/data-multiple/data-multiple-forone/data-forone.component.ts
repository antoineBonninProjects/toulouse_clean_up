import { Component } from '@angular/core';
import { OnInit } from '@angular/core';

import { DataMultipleForOneService } from "./data-forone.service";


@Component({
	selector: 'data-forone',
  	templateUrl: './data-forone.component.html',
	providers: [DataMultipleForOneService],
})
export class DataMultipleForOneComponent implements OnInit{
	allDataForOne: any;

	constructor (private _dataService: DataMultipleForOneService) {
	}

	ngOnInit():any {
		this._dataService.getAllForOne().subscribe(
				data => this.allDataForOne = data['json_list'],
				error => alert(error),
				() => console.log("Finished !")
			);

		this._dataService.listen('weight_update').subscribe(res => {
			var len = Object.keys(this.allDataForOne).length;
			this.allDataForOne[len] = ({"device_id":res.device_id,
			                            "seq_num":res.seq_num,
			                            "weight":res.weight});
		});
	}
};
