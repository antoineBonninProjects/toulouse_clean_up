import {Injectable} from 'angular2/core';
import {Http} from 'angular2/http';
import 'rxjs/add/operator/map';

@Injectable()
export class CounterService {
	constructor (private _http: Http) {}

	getLatestWeight() {
		return this._http.get('http://172.20.10.10:5000/api/get_sigfox_messages/latest/weight/1D1901').map(res => res.json());
	}
}
