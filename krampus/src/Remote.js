import RemoteButton from './RemoteButton';
import {KeyboardArrowUp, KeyboardArrowDown, Brightness7, Brightness3, Loop} from '@mui/icons-material';

const Styles = {
    borderColor: "#333",
    borderStyle: 'solid',
    borderWidth: '3px',
    borderRadius: '15px',
    marginBottom: '5px',
    padding: '10px',
    width: "270px",
    boxShadow: "rgba(50, 50, 93, 0.25) 0px 30px 60px -12px, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px"
}

const Buttons = [
    { color: "#FF0000", textColor: '#FFF', text: "On",              icon: null,                 action: "On" },
    { color: "#000000", textColor: '#FFF', text: "Off",             icon: null,                 action: "Off" },
    { color: "#ffffff", textColor: '#fff', text: "",                icon: null,                 action: "blank" },
    { color: "#ffffff", textColor: '#000', text: "Loop",            icon: Loop,                 action: "Loop" },
    { color: "#ffffff", textColor: '#000', text: "Delay Up",        icon: KeyboardArrowUp,      action: "DelayUp" },
    { color: "#ffffff", textColor: '#000', text: "Delay Dn",        icon: KeyboardArrowDown,    action: "DelayDn" },
    { color: "#ffffff", textColor: '#000', text: "Brightnes Dn",    icon: Brightness3,          action: "BrightnessDn" },
    { color: "#ffffff", textColor: '#000', text: "Brightness Up",   icon: Brightness7,          action: "BrightnessUp" },
    { color: "#FF0000", textColor: '#FFF', text: "R",               icon: null,                 action: "SetTreeColor" },
    { color: "#00FF00", textColor: '#FFF', text: "G",               icon: null,                 action: "SetTreeColor" },
    { color: "#0000FF", textColor: '#FFF', text: "B",               icon: null,                 action: "SetTreeColor" },
    { color: "#FFFFFF", textColor: '#000', text: "W",               icon: null,                 action: "SetTreeColor" },
    { color: "#ff3333", textColor: '#FFF', text: "",                icon: null,                 action: "SetTreeColor" },
    { color: "#33ff33", textColor: '#FFF', text: "",                icon: null,                 action: "SetTreeColor" },
    { color: "#3333ff", textColor: '#FFF', text: "",                icon: null,                 action: "SetTreeColor" },
    { color: "#FFEE58", textColor: '#FFF', text: "",                icon: null,                 action: "SetTreeColor" },
    { color: "#ff6666", textColor: '#FFF', text: "",                icon: null,                 action: "SetTreeColor" },
    { color: "#66ff66", textColor: '#FFF', text: "",                icon: null,                 action: "SetTreeColor" },
    { color: "#6666ff", textColor: '#FFF', text: "",                icon: null,                 action: "SetTreeColor" },
    { color: "#ffa500", textColor: '#FFF', text: "",                icon: null,                 action: "SetTreeColor" },
    { color: "#800080", textColor: '#FFF', text: "",                icon: null,                 action: "SetTreeColor" },
    { color: "#40E0D0", textColor: '#FFF', text: "",                icon: null,                 action: "SetTreeColor" },
];

const apiActions = {
    "On": "/api/start",
    "Off": "/api/stop",
    "Loop": "/api/loop",
    "SetTreeColor": "/api/color/change/",
    "DelayUp": "/api/delayUp",
    "DelayDn": "/api/delayDown",
    "BrightnessUp": "/api/brightnessUp",
    "BrightnessDn": "/api/brightnessDown"
};

async function fetchAsync(url) {
    let response = await fetch(url);
    let data = await response.text();
    return JSON.parse(data);
  }

function Remote() {

    let buttonClicked = async(buttonData) => {
        console.log(buttonData.action);
        let apiUrl = apiActions[buttonData.action]
        console.log("ApiUrl: " + apiUrl);
        if (apiUrl) {
            if (buttonData.action === "SetTreeColor") {
                console.log("Color " + buttonData.color);
                apiUrl = apiUrl + encodeURIComponent(buttonData.color)
            }

            let response = await fetchAsync(apiUrl);
            console.log(response);
        }
    }

  return (
    <div style={Styles} class="remote">
        {
            Buttons.map(button => {
                return <RemoteButton color={button.color} data={button} textColor={button.textColor} text={button.text} onClick={buttonClicked} />
            })
        }
        <div style={{clear: "both"}}></div>
    </div>
  );
}

export default Remote;
