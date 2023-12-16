<header class="navbar">
    <section class="navbar-section"> 
        <h2> devices </h2> 
    </section>
    <section class="navbar-section">
        <div class="input-group input-inline">
            <button class="btn btn-primary input-group-btn" onclick="openNewDevice()">
                <i class="icon icon-plus"></i> New Device
            </button>
        </div>
        <div class="input-group input-inline">
            <input class="form-input" type="search" onsearch="search()" placeholder="search" id="search">
            <button class="btn btn-primary input-group-btn" onclick="search()">
                <i class="icon icon-search"></i>
            </button>
        </div>
    </section>
</header>


<div class="container" id="device-list"> 
    <div class="loading loading-lg"></div>
</div>    
<script type="module" src="/static/js/deviceList.js"></script>