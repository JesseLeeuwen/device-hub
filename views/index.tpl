<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <link rel="stylesheet" href="/static/css/spectre.min.css">
    <link rel="stylesheet" href="/static/css/spectre-icons.min.css">
    <link rel="stylesheet" href="/static/css/spectre-exp.min.css">

    <link href='https://unpkg.com/css.gg@2.0.0/icons/css/screen.css' rel='stylesheet'>

    <link rel="stylesheet" href="/static/css/main.css">
    
    <script src="/static/js/device.js"></script>
</head>
<body>
    <div class="hero">
        <div class="hero-body">
            <h1>Jesse home office management</h1>
            <p>manage and see devices</p>
        </div>
    </div>
    
    <div class="modal " id="modal-new-device">
        <a href="#close" class="modal-overlay" aria-label="Close"></a>
        <div class="modal-container">
            <div class="modal-header">
                <a href="#close" class="btn btn-clear float-right" aria-label="Close" onclick="closeNewDevice()"></a>
                <div class="modal-title h5">New Device</div>
            </div>
            <div class="modal-body">
            <div class="content">
                <form id="form-new-device" class="form-horizontal"  action="javascript:newDevice();" >
                    <div class="form-group"> 
                        <div class="col-3">
                            <label for="device-name">Name</label>
                        </div>
                        <div class="col-9">
                            <input type="text" class="form-input" name="device-name" id="device-name" required>
                        </div>
                    </div>
                    <div class="form-group"> 
                        <div class="col-3">
                            <label for="device-mac">Mac Address</label>
                        </div>
                        <div class="col-9">
                            <input type="text" class="form-input" name="device-mac" id="device-mac" required>
                        </div>
                    </div>
                </form>
            </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-primary input-group-btn" onclick="submit()" > Add Device </button>
            </div>
        </div>
    </div>
    
    % if len(devices) == 0:
        % include('components/empty.tpl' )
    % end
    % if len(devices) > 0:
        % include('components/devices.tpl')
    % end
</body>
</html>