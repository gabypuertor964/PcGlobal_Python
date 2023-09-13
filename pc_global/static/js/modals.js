const windowBackground = document.getElementById('window-background');
const windowContainer = document.getElementById('window-container');
const openButton = document.getElementById('modal-actualizar');
const closeButton = document.getElementById('close-button');

// variables para el modal de borrar reporte
const windowBackgroundDelete = document.getElementById('window-background-del');
const windowContainerDelete = document.getElementById('window-background-del'); 
const openButtonDelete = document.getElementById('modal-borrar');
const closeButtonDelete = document.getElementById('close-button-del')

// configuracion boton de actualizar reporte
openButton.addEventListener('click', ()=>windowBackground.style.display='flex')

const closeWindow = () => {
    windowContainer.classList.add('close')

    setTimeout(() => {
        windowContainer.classList.remove('close')
        windowBackground.style.display = 'none'
    }, 1000)
}

closeButton.addEventListener('click', ()=>closeWindow())

// configuracion boton de borrar reporte


openButtonDelete.addEventListener('click', ()=>windowBackgroundDelete.style.display='flex')

const closeWindowDelete = () => {
    windowContainerDelete.classList.add('close')

    setTimeout(() => {
        windowContainerDelete.classList.remove('close')
        windowBackgroundDelete.style.display = 'none'
    }, 1000)
}

closeButtonDelete.addEventListener('click', () => closeWindowDelete())

const windowBackgroundView = document.getElementById('window-background-view')
const windowContainerView= document.getElementById('window-background-view'); 
const openButtonView = document.getElementById('button-view');
const closeButtonview = document.getElementById('close-button-view')

openButtonView.addEventListener('click', ()=> windowBackgroundView.style.display='flex')

const closeWindowView = () => {
    windowContainerView.classList.add('close')

    setTimeout(() => {
        windowContainerView.classList.remove('close')
        windowBackgroundView.style.display = 'none'
    }, 1000)
}

closeButtonview.addEventListener('click', () => closeWindowView())