function openNewDevice()
{
    let modal = document.querySelector( "#modal-new-device" )
    modal.classList.add("active")
}

function closeNewDevice()
{
    document.querySelector( "#form-new-device" ).reset()
    let modal = document.querySelector( "#modal-new-device" )
    modal.classList.remove("active")
}

function submit()
{
    document.querySelector( "#form-new-device" ).requestSubmit()
}

function search()
{
    window.api.fetch( document.querySelector("#search").value )
}

async function newDevice()
{
    let form = document.querySelector( "#form-new-device" )   
    let response = await fetch( "/devices/new", {
        method: "POST",
        body: new FormData(form)
    } )
    
    window.location.reload()
}

async function removeDevice(name, mac)
{
    if( !confirm( `do you want to remove ${name}?`, "yes", "no" ) )
        return

    await fetch(`/devices/${name}/remove`, {method: "DELETE"})
    window.api.fetch()
}

async function wolSignal(name, mac)
{
    console.log("hoi")
    await fetch(`/devices/${name}/startup`, {method: "POST"})
}