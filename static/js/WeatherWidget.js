function weather_button(){
    const widget = document.getElementById('weather-widget');
    const arrow = document.querySelector('.arrow-button');
    const widgetTranslate = document.getElementById('weather-widget-translate')
  
    if ( widget.classList.contains('opened') ){
      widgetTranslate.style.transform = 'translateX(-10%)'
      setTimeout(()=>{
        arrow.innerHTML='&nbsp;<'
        widgetTranslate.style.borderTopRightRadius = '12px'
        widgetTranslate.style.borderBottomRightRadius = '12px'
      },700)
    }
    else{
      widgetTranslate.style.transform = 'translateX(-100%)'
      setTimeout(()=>{
        arrow.innerHTML='&nbsp;>'
        widgetTranslate.style.borderTopRightRadius = '0px'
        widgetTranslate.style.borderBottomRightRadius = '0px'
      },800)
  
    }
  
    widget.classList.toggle('opened');
  }