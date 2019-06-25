var renderTasks = function () {
    var request = {
        method: 'GET',
        url: '/todo/all',
        data: '',
        dataType: "json",
        success: function(response) {
            // log('response', response)
            clearTasks()
            showTasks(response)
        }
    }
    $.ajax(request)
}

var clearTasks = function () {
    var todos = $('.todo')
    todos.remove()
}

var showTasks = function (response) {
    var htmls = []
    for (var i = 0; i < response.length; i++) {
        var id = response[i].id
        var t = response[i].task
        var done = response[i].done
        log(done)
        var template = templateTask(id, t, done)
        htmls.push(template)
    }
    for (var i = 0; i < htmls.length; i++) {
        var h = htmls[i]
        $('content').append(h)
    }
}

var templateTask = function (id, task, done) {
    var d = ''
    if (done === '1') {
        var d = 'done'
    }
    var t = `
    <div class="todo ${d}" data-id=${id}>
        <button class="btn-done">Done</button>
        <button class="btn-delete">Delete</button>
        <span>${task}</span>
    </div>
    `
    return t
}

var addTask = function () {
    $('#id-btn-add').on('click', function () {
        var task = $('#id-input').val()
        // var html = templateTask(id, task)
        var userID = $('#user-id').val()
        // $('content').append(html)
        addToDB(task, userID)
        renderTasks()
    })
}

var addToDB = function (task, userID) {
    var data = {
        task: `${task}`,
        user_id: `${userID}`,
    }
    var request = {
        method: 'POST',
        url: '/todo/add',
        data: data,
        // dataType: "json",
        success: function(response) {
            log('response', response)
        }
    }
    $.ajax(request)
}

var deleteTask = function () {
    $('content').on('click', '.btn-delete', function (e) {
        var target = e.target
        var todo = target.closest('.todo')
        var id = todo.dataset.id
        // log(typeof id)
        deleteFromDB(id)
        renderTasks()
    })
}

var deleteFromDB = function (id) {
    var request = {
        method: 'GET',
        url: `/todo/delete/${id}`,
        dataType: "json",
        success: function(response) {
            log('response', response)
        }
    }
    $.ajax(request)
}

var addToDB = function (task, userID) {
    var data = {
        task: `${task}`,
        user_id: `${userID}`,
    }
    var request = {
        method: 'POST',
        url: '/todo/add',
        data: data,
        // dataType: "json",
        success: function(response) {
            log('response', response)
        }
    }
    $.ajax(request)
}

var doneTask = function () {
    $('content').on('click', '.btn-done', function (e) {
        var target = e.target
        var todo = target.closest('.todo')
        var id = todo.dataset.id
        var done = 0
        todo = $(todo)
        todo.toggleClass('done')
        if (todo.hasClass('done')) {
            done = 1
        }
        doneFromDB(id, done)
        renderTasks()
    })
}

var doneFromDB = function (id, done) {
    data = {
        id: id,
        done: done,
    }
    var request = {
        method: 'POST',
        url: '/todo/done',
        data: data,
        dataType: "json",
        success: function(response) {
            log('response', response)
        }
    }
    $.ajax(request)
}

var __main = function () {
    renderTasks()
    addTask()
    deleteTask()
    doneTask()
}

__main()
