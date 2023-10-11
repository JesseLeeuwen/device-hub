import { reactive, html } from 'https://esm.sh/@arrow-js/core';

const data = reactive({
    devices: []
}) 

const template = html`${() => data.devices.map( device => html`
<div class="tile tile-centered">
    <div class="tile-icon">
        <figure class="avatar avatar-xl">
            <i class="gg-screen"></i>
            <i class="avatar-presence ${device.state? "online" : ""} "></i>
        </figure>
    </div>
    <div class="tile-content">
        <div class="tile-title"> ${device.name} </div>
        <small class="tile-subtitle text-gray">${device.mac} · last online · ${device.state? "now" : device.lastOnline}</small>
    </div>
    <div class="tile-action dropdown ">
        <button class="btn btn-link dropdown-toggle" tabindex="0" > 
            <i class="icon icon-more-vert"></i>
        </button>
        <ul class="menu">
            <li class="menu-item">
                <a href="#" onclick="wolSignal('${device.name}', '${device.mac}')">send WOL signal</a>
            </li>  
            <li class="menu-item">
                <a href="#" onclick="removeDevice('${device.name}', '${device.mac}')" >Remove</a>
            </li>  
        </ul>
    </div>
</div>
<div class="divider"></div>
`)}`;

template( document.querySelector( "#device-list" ) )

// fetch devices
window.api = {}
window.api.fetchFilter = ""
window.api.fetch = fetchDevices

setTimeout(() => {
    fetchDevices("")
}, 50);

setInterval(() => {
    if( document.hasFocus() )
        fetchDevices( window.api.fetchFilter )
}, 3000);

// ----------------------------------------------------

async function fetchDevices( filter )
{
    // new search
    if( filter != window.api.fetchFilter )
        window.api.fetchFilter = filter

    const query = window.api.fetchFilter
    const response = await fetch( "/devices/list?filter="+query )
    const json = await response.json()
    data.devices = json
}  