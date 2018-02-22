import {Component} from 'angular2/core';
import {CounterComponent} from "./counter.component"


@Component({
    selector: 'my-app',
    template: `
    	<h1>Main page header</h1>
    	<p>Toulouse Clean Up Start</p>
    	<h2>Below comes the counter component</h2>
    	<counter>Loading counter component...</counter>
    `,
    directives: [CounterComponent]
})
export class AppComponent {

}