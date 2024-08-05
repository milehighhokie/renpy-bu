init python:

    class Cards(object):
        def __repr__(self):
            return 'order = %r,%r,%r,%r,%r,%r' % (self.order[0].cards[0], self.order[1].cards[0], self.order[2].cards[0],self.order[3].cards[0],self.order[4].cards[0],self.order[5].cards[0])
            
        def __init__(self, deal=3):

            # Constants that let us easily change where the game is
            # located.
            LEFT=90
            TOP=58
            COL_SPACING = 90
            ROW_SPACING = 120
            CARD_XSPACING = 20
            CARD_YSPACING = 30

            # Store the parameters.
            self.deal = deal
            
            # Create the table and stack
            self.table = t = Table(base="cards/empty_spot.png")
            self.stack = t.stack(-5000, -5000, xoff=0, yoff=0, click=False)

            # The order places
            self.order = [ ]
            for i in range(0, 6):
                s = t.stack(LEFT + COL_SPACING * (i + 1), TOP, xoff=0, yoff=0, drag=DRAG_TOP, drop=True)
                self.order.append(s)

            # The initial card places
            self.start = [ ]
            for i in range(0, 8):
                s = t.stack(LEFT + COL_SPACING * i, TOP + ROW_SPACING, xoff=0, yoff=CARD_YSPACING, drag=DRAG_ABOVE, click=True, drop=True)
                self.start.append(s)

            # Create the stack and shuffle it.
            for value in range(1, 9):
                t.card(value, "cards/%d.png" % value )
                t.set_faceup(value, True)
                self.stack.append(value)
                    
            self.stack.shuffle()
            
            # Deal out the cards
            for i in range(0, 8):
                c = self.stack.deal()
                self.start[i].append(c)                    
                
        def show(self):
            self.table.show()

        def hide(self):
            self.table.hide()
            
        def start_drag(self, evt):
            # If the stack is empty, allow a card to be dragged to it.
            if len(evt.drop_stack) == 0:
                evt.drop_stack.append(evt.drag_cards[0])
                return "start_drag"

            return False
                    
        def order_drag(self, evt):
            # If there is not a card on the order already, allow drag
            if len(evt.drop_stack) == 0:
                evt.drop_stack.append(evt.drag_cards[0])
                return "order_drag"

            return False

                    
        def interact(self):

            evt = ui.interact()
            rv = False
            
            # Check the drag events
        #    if evt.type == "drag":
            if evt.drop_stack in self.start:
                rv = self.start_drag(evt)
                
            elif evt.drop_stack in self.order:
                rv = self.order_drag(evt)

            else :
                rv = self.evt.drop_stack
                    
            # Check to see if any of the order has less than
            # 13 cards in it. If it does, return False. Otherwise,
            # return True.
            ##for i in self.order:
            ##    if len(i) != 13:
            return rv

            ##return "win"

        # Sets things as sensitive (or not).
        #def set_sensitive(self, value):
        #    self.table.set_sensitive(value)

        # Returns the first faceup card in the stack.
        def first_faceup(self, s):
            for c in s:
                if self.table.get_faceup(c):
                    return c


                     
                    
