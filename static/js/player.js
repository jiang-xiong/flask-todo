var data = {
    songs: [
        {
            name: 'La Vanille',
            author: '茶理理',
        },
        {
            name: 'Slippin',
            author: 'Taylor Thrash',
        },
        {
            name: 'Rain',
            author: '秦基博',
        },
    ],
    showMenu: true,
    showPlay: true,
    showPause: false,
    name: 'La Vanille',
    author: '茶理理',
    showVolume: false,
}

var log = console.log.bind(console)

var e = function(selector) {
    return document.querySelector(selector)
}

var bindEvent = function(element, eventName, callback) {
    element.addEventListener(eventName, callback)
}

var removeClassAll = function(className) {
    var selector = '.' + className
    var elements = document.querySelectorAll(selector)
    for (var i = 0; i < elements.length; i++) {
        var e = elements[i]
        e.classList.remove(className)
    }
}

var toggleClass = function(element, className) {
    if (element.classList.contains(className)) {
        element.classList.remove(className)
    } else {
        element.classList.add(className)
    }
}

var play = function () {
    this.showPlay = false
    this.showPause = true
    var audio = e('audio')
    audio.play()
}

var pause = function () {
    this.showPlay = true
    this.showPause = false
    var audio = e('audio')
    // log('click audio', audio)
    audio.pause()
}

var updateBar = function () {
    var music = e('audio')
    var currentTime = (music.currentTime / music.duration) * 100
    var intCurrentTime = Math.trunc(currentTime)
    // log('intCurrentTime', intCurrentTime)
    var processBar = e('#ctrl-bar')
    processBar.value = currentTime
    var s = document.createElement('style')
    s.innerText = `
    #ctrl-bar::-webkit-slider-runnable-track {
    background:linear-gradient(to right, gray 5%, gray ${intCurrentTime}%, #eee 0%);
    }
    `
    document.body.appendChild(s)
}

var bindScrollBar = function () {
    var music = e('audio')
    bindEvent(music, 'timeupdate', updateBar)
}

var changeVolume = function () {
    var volume = e('#id-volume-bar')
    // log('volume value', volume.value)
    var audio = e('audio')
    audio.volume = volume.value / 100
}

var bindChangeBar = function () {
    var processBar = e('#ctrl-bar')
        bindEvent(processBar, 'input', function (event) {
        var currentProcessBar = event.target.value
        // log('currentProcessBar', currentProcessBar)
        var music = e('audio')
        music.removeEventListener('timeupdate', updateBar)
        music.currentTime = music.duration * (currentProcessBar / 100)
        music.play()
        bindScrollBar()
    })
}

var toggleMenu = function () {
    this.showMenu = !this.showMenu
    // log(this.showMenu)
}

var toggleVolume = function () {
    this.showVolume = !this.showVolume
    // log(this.showMenu)
}

var changeSong = function (event) {
    var target = event.target
    removeClassAll('active')
    toggleClass(target, 'active')

    var a = target.innerText.split(' - ')
    var name = a[0]
    var author = a[1]

    this.name = name
    this.author = author

    var cover = e('#cover')
    var src = '/static/img/music/' + name + '-' + author + '.jpg'
    cover.src = src

    var src = '/static/mp3/' + name + '-' + author + '.mp3'
    var audio = e('audio')
    audio.src = src
    this.showPlay = false
    this.showPause = true
    audio.play()
}

var changeInfo = function () {

}

var vm = new Vue({
    el: '#app',
    delimiters: ['{[', ']}'],
    data: data,
    methods: {
        play,
        pause,
        changeVolume,
        toggleMenu,
        changeSong,
        toggleVolume,
    },
    mounted() {
        bindScrollBar()
        bindChangeBar()
    },

})
