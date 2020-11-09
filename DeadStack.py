#container that stores cards in a dead stack

class DeadStack:
    Stack c = []
    def __init__(self, unplayable):
        c = flipStack(unplayable)

    def flipStack(Stack):
        if not isEmpty(Stack):
            temp = pop(Stack)
            flipStack(Stack)
            insertAtBottom(Stack, temp)

    def insertAtBottom(stack, i):
        if isEmpty(stack):
            push(stack, i)
        else:
            temp = pop(stack)
            insertAtBottom(stack, i)
            push(stack, temp)

    def getStatus():
        return 1