import { Textfit } from 'react-textfit';

let BaseStyle = {
    borderRadius: '50%',
    borderColor: "#000",
    borderWidth: '1px',
    borderStyle: 'solid',
    backgroundColor: '#000',
    color: '#fff',
    cursor: 'pointer',
    float: 'left',
    height: '50px',
    lineHeight: '30px',
    margin: '5px',
    padding: '10px',
    width: '50px',
};

let activeStyle = {
    borderColor: "#FFF",
    transform: 'scale(0.98)',
    boxShadow: '3px 2px 22px 1px rgba(0, 0, 0, 0.24)'
};

function RemoteButton(props) {
    let componentStyle = {...BaseStyle}
    componentStyle.backgroundColor = props.color
    componentStyle.color = props.textColor

    if (props.data.icon) {
        componentStyle.lineHeight = '5px';
        componentStyle.padding = '0px';
    }

    if (props.data.action === 'blank') {
        componentStyle.borderColor = "#fff";
        componentStyle.cursor = 'default';
    }

    let onClickHandler = (e) => {
        if (props.onClick) {
            props.onClick(props.data);
        }
    }
    
    return (
    <div style={componentStyle} activeStyle={activeStyle} onClick={onClickHandler}>
        <Textfit mode="single">
            {props.data.icon ? <props.data.icon /> : props.text}
        </Textfit>
    </div>
  );
}

export default RemoteButton;
