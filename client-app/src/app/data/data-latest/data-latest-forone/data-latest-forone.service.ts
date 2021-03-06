import {Injectable} from '@angular/core';
import {Http} from '@angular/http';
import 'rxjs/add/operator/map';
import {Observable} from 'rxjs/Observable';

import * as io from 'socket.io-client';
import {BehaviorSubject} from 'rxjs/BehaviorSubject';

@Injectable()
export class DataLatestForOneService {
	socket: any;
	socketConnected$ = new BehaviorSubject<boolean>(false);
	
	server_IP = "172.20.10.10"
	server_port = "5000"
	server_url = 'http://'+ this.server_IP + ':' + this.server_port

	constructor (private _http: Http) {
		this.socket = io(this.server_url, {});
		this.socket.on('connect', () => this.socketConnected$.next(true));
		this.socket.on('disconnect', () => this.socketConnected$.next(false));

		this.socketConnected$.asObservable().subscribe( connected => {
     		console.log('Socket connected: ', connected);
		});
	}

	getLatestWeight() {
		return this._http.get(this.server_url + '/api/get_sigfox_messages/latest/weight/1D1901').map(res => res.json());
	}

	listen(event: string): Observable<any> {

	    return new Observable(observer => {
	    		this.socket.on(event, data => {
	    			observer.next(data);
	    		});

	      		// observable is disposed
	      		return () => {
	        		this.socket.off(event);
				}
		});
	}
}