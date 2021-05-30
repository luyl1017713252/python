$('.title').click(function () {
    $(this).next().attr('class', 'body')
    $(this).parent().siblings().children('.body').addClass('hide')
})