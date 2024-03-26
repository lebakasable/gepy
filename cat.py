import ge

cat = ge.new_text('=^.^=', font_size=70)


@ge.repeat_forever
async def move_cat():
    cat.x = ge.random_number(-200, 200)
    cat.y = ge.random_number(-200, 200)
    cat.color = ge.random_color()

    cat.show()

    await ge.timer(seconds=0.4)

    cat.hide()

    await ge.timer(seconds=0.4)


@cat.when_clicked
def win_function():
    cat.show()
    cat.words = 'You won!'


ge.start_program()
