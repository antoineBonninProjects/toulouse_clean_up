import {Component} from 'angular2/core';
import {OnInit} from 'angular2/core';

import {CounterService} from "./counter.service";

@Component({
	selector: 'counter',
	template: `
		<h1>This is my Counter</h1>
		<p>
		<br>
			<span [class.default_count_style]="1" [class.other_count_style]="input.value === 'yes'">{{count}}</span>
		<br>
		wanna change color?
		<input type="text" #input (keyup)="0">
		</p>
	`,
	styleUrls: ['src/css/counter.css'],
	providers: [CounterService]
})
export class CounterComponent implements OnInit{
	count;

	constructor (private _counterService: CounterService) {}

	ngOnInit():any {
		this.count = this._counterService.getLatestWeight().subscribe(
				data => this.count = JSON.parse(JSON.stringify(data)).weight,
				error => alert(error),
				() => console.log("Finished !")
			);
	}
} 




