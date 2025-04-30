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
    document.activeElement.blur()
    if( !confirm( `do you want to remove ${name}?`, "yes", "no" ) )
        return

    await fetch(`/devices/${name}/remove`, {method: "DELETE"})
    window.api.fetch()
}

async function wolSignal(name, mac)
{
    console.log("hoi")
    document.activeElement.blur()
    await fetch(`/devices/${name}/startup`, {method: "POST"})
}

async function shutdownSignal(name)
{
    console.log("doei")
    document.activeElement.blur()
    
    await fetch(`/devices/${name}/shutdown`, {method: "POST"})
}