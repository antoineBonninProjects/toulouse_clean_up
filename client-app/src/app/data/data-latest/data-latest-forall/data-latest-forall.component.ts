import { Component } from '@angular/core';
import { OnInit } from '@angular/core';

import { DataLatestForallService } from "./data-latest-forall.service";


@Component({
	selector: 'data-latest-forall',
  	templateUrl: './data-latest-forall.component.html',
	providers: [DataLatestForallService],
})
export class DataLatestForallComponent implements OnInit{
	latestDataForall: any;

	constructor (private _dataService: DataLatestForallService) {
	}

	ngOnInit():any {
		this._dataService.getLatestForall().subscribe(
				data => this.latestDataForall = data['json_list'],
				error => alert(error),
				() => console.log("Finished !")
			);

		this._dataService.listen('weight_update').subscribe(res => {
			var found:boolean = false;
			for (var device_info of this.latestDataForall) {
				if (device_info.device_id == res.device_id) {
					device_info.seq_num  = res.seq_num;
					device_info.weight  = res.weight;
					found = true;
				}
			}
			if (found != true) {
			    var len = Object.keys(this.latestDataForall).length;
			    this.latestDataForall[len] = ({"device_id":res.device_id,
			                                     "seq_num":res.seq_num,
			                                     "weight":res.weight});
			    }
		});
	}
};
