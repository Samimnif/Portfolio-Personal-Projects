 import java.util.Stack;

/**
 *  Assignment 4
 *  Used the provided sample solution to assignment 3.
 * 
 *  This class is the main class of the "World of Zuul" application. 
 *  "World of Zuul" is a very simple, text based adventure game.  Users 
 *  can walk around some scenery. That's all. It should really be extended 
 *  to make it more interesting!
 * 
 *  To play this game, create an instance of this class and call the "play"
 *  method.
 * 
 *  This main class creates and initialises all the others: it creates all
 *  rooms, creates the parser and starts the game.  It also evaluates and
 *  executes the commands that the parser returns.
 * 
 * @author  Michael Kolling and David J. Barnes 
 * @version 2006.03.30
 * 
 * @author Lynn Marshall
 * @version A3 Solution
 * 
 * @author Sami Mnif (101199669)
 * @version 2022.03.19
 */

public class Game 
{
    private Parser parser;
    private Room currentRoom;
    private Room previousRoom;
    private Stack<Room> previousRoomStack;
    // item being held by the player
    private Item itemHeld;
    // number of items that can be cariied before food needed
    private int numberHeld;
        
    /**
     * Create the game and initialise its internal map, as well
     * as the previous room (none) and previous room stack (empty).
     * Sets the item held is as none and sets the number of items can be 
     * carried as 0 (needs to eat first).
     */
    public Game() 
    {
        createRooms();
        parser = new Parser();
        previousRoom = null;
        previousRoomStack = new Stack<Room>();
        itemHeld = null; //sets the item held as null (means nothing)
        numberHeld = 0; //intial number as 0 (needs to eat cookie first)
    }

    /**
     * Create all the rooms and link their exits together.
     */
    private void createRooms()
    {
        Room outside, theatre, pub, lab, office, transporter;
        Item chair1, chair2, chair3, chair4, bar, computer1, computer2, computer3,
        tree1, tree2, cookie1, cookie2, cookie3, cookie4, beamer1, beamer2;
        
        // create some items
        chair1 = new Item("chair","a wooden chair",5);
        chair2 = new Item("chair","a wooden chair",5);
        chair3 = new Item("chair","a wooden chair",5);
        chair4 = new Item("chair","a wooden chair",5);
        bar = new Item("bar","a long bar with stools",95.67);
        computer1 = new Item("pc","a PC",10);
        computer2 = new Item("mac","a Mac",5);
        computer3 = new Item("pc","a PC",10);
        tree1 = new Item("tree","a fir tree",500.5);
        tree2 = new Item("tree","a fir tree",500.5);
        cookie1 = new Item("cookie", "a delicious chocolate cookie", 0.5);
        cookie2 = new Item("cookie", "a delicious chocolate cookie", 0.5);
        cookie3 = new Item("cookie", "a delicious chocolate cookie", 0.5);
        cookie4 = new Item("cookie", "a delicious chocolate cookie", 0.5);
        beamer1 = new Beamer();
        beamer2 = new Beamer();
       
        // create the rooms
        outside = new Room("outside the main entrance of the university");
        theatre = new Room("in a lecture theatre");
        pub = new Room("in the campus pub");
        lab = new Room("in a computing lab");
        office = new Room("in the computing admin office");
        transporter = new TransporterRoom();
        
        // put items in the rooms
        outside.addItem(tree1);
        outside.addItem(tree2);
        theatre.addItem(chair1);
        theatre.addItem(cookie1);
        pub.addItem(bar);
        pub.addItem(beamer1);
        lab.addItem(chair2);
        lab.addItem(computer1);
        lab.addItem(chair3);
        lab.addItem(computer2);
        lab.addItem(cookie2);
        office.addItem(chair4);
        office.addItem(computer3);
        office.addItem(cookie3);
        office.addItem(beamer2);
        transporter.addItem(cookie4);
        
        // initialise room exits
        outside.setExit("east", theatre); 
        outside.setExit("south", lab);
        outside.setExit("west", pub);

        theatre.setExit("west", outside);

        pub.setExit("east", outside);

        lab.setExit("north", outside);
        lab.setExit("east", office);
        lab.setExit("west", transporter);

        office.setExit("west", lab);
        
        transporter.setExit("anywhere", null);

        currentRoom = outside;  // start game outside
    }

    /**
     *  Main play routine.  Loops until end of play.
     */
    public void play() 
    {            
        printWelcome();

        // Enter the main command loop.  Here we repeatedly read commands and
        // execute them until the game is over.
                
        boolean finished = false;
        while (! finished) {
            Command command = parser.getCommand();
            finished = processCommand(command);
        }
        System.out.println("Thank you for playing.  Good bye.");
    }

    /**
     * Print out the opening message for the player.
     */
    private void printWelcome()
    {
        System.out.println();
        System.out.println("Welcome to the World of Zuul!");
        System.out.println("World of Zuul is a new, incredibly boring adventure game.");
        System.out.println("Type 'help' if you need help.");
        System.out.println();
        System.out.println(printRoomAndCarry());
    }

    /**
     * Given a command, process (that is: execute) the command.
     * 
     * @param command The command to be processed
     * @return true If the command ends the game, false otherwise
     */
    private boolean processCommand(Command command) 
    {
        boolean wantToQuit = false;

        if(command.isUnknown()) {
            System.out.println("I don't know what you mean...");
            return false;
        }

        String commandWord = command.getCommandWord();
        if (commandWord.equals("help")) {
            printHelp();
        }
        else if (commandWord.equals("go")) {
            goRoom(command);
        }
        else if (commandWord.equals("quit")) {
            wantToQuit = quit(command);
        }
        else if (commandWord.equals("look")) {
            look(command);
        }
        else if (commandWord.equals("eat")) {
            eat(command);
        }
        else if (commandWord.equals("back")) {
            back(command);
        }
        else if (commandWord.equals("stackBack")) {
            stackBack(command);
        }
        else if (commandWord.equals("take")) {
            take(command);
        }
        else if (commandWord.equals("drop")) {
            drop(command);
        }
        else if (commandWord.equals("charge")) {
            charge(command);
        }
        else if (commandWord.equals("fire")) {
            fire(command);
        }
        // else command not recognised.
        return wantToQuit;
    }

    // implementations of user commands:

    /**
     * Print out some help information.
     * Here we print a cryptic message and a list of the 
     * command words.
     */
    private void printHelp() 
    {
        System.out.println("You are lost. You are alone. You wander");
        System.out.println("around at the university.");
        System.out.println();
        System.out.println("Your command words are:");
        System.out.println(parser.getCommands());
    }

    /** 
     * Try to go to one direction. If there is an exit, enter the new
     * room, otherwise print an error message.
     * If we go to a new room, update previous room and previous room stack.
     * 
     * @param command The command to be processed
     */
    private void goRoom(Command command) 
    {
        if(!command.hasSecondWord()) {
            // if there is no second word, we don't know where to go...
            System.out.println("Go where?");
            return;
        }

        String direction = command.getSecondWord();

        // Try to leave current room.
        Room nextRoom = currentRoom.getExit(direction);

        if (nextRoom == null) {
            System.out.println("There is no door!");
        }
        else {
            previousRoom = currentRoom; // store the previous room
            previousRoomStack.push(currentRoom); // and add to previous room stack
            currentRoom = nextRoom;
            System.out.println(printRoomAndCarry());
        }
    }

    /** 
     * "Quit" was entered. Check the rest of the command to see
     * whether we really quit the game.
     * 
     * @param command The command to be processed
     * @return true, if this command quits the game, false otherwise
     */
    private boolean quit(Command command) 
    {
        if(command.hasSecondWord()) {
            System.out.println("Quit what?");
            return false;
        }
        else {
            return true;  // signal that we want to quit
        }
    }
    
    /** 
     * "Look" was entered. Check the rest of the command to see
     * whether we really want to look.
     * 
     * @param command The command to be processed
     */
    private void look(Command command) 
    {
        if(command.hasSecondWord()) {
            System.out.println("Look what?");
        }
        else {
            // output the long description of this room
            System.out.println(printRoomAndCarry());
        }
    }
    
    /** 
     * "Eat" was entered. Checks if we have food and eat it. When successful,
     * sets the number of items can be carried to 5 and removed the item from
     * carry. Prints the message.
     * 
     * @param command The command to be processed
     */
    private void eat(Command command) 
    {
        if(command.hasSecondWord()) {
            System.out.println("Eat what?");
        }
        else {
            if (itemHeld == null)
            {
                System.out.println("You are not holding anything :(");
            }
            else if (itemHeld.getName().equals("cookie"))
            {
                itemHeld = null;
                numberHeld = 5;
                System.out.println("You ate a chocolate cookie. You gained strength");
            }
            else
            {
                System.out.println("You don't have any food :(");
            }
        }
    }
    
    /** 
     * "Back" was entered. Check the rest of the command to see
     * whether we really quit the game.
     * 
     * @param command The command to be processed
     */
    private void back(Command command) 
    {
        if(command.hasSecondWord()) {
            System.out.println("Back what?");
        }
        else {
            // go back to the previous room, if possible
            if (previousRoom==null) {
                System.out.println("No room to go back to.");
            } else {
                // go back and swap previous and current rooms,
                // and put current room on previous room stack
                Room temp = currentRoom;
                currentRoom = previousRoom;
                previousRoom = temp;
                previousRoomStack.push(temp);
                // and print description
                System.out.println(printRoomAndCarry());
            }
        }
    }
    
    /** 
     * "StackBack" was entered. Check the rest of the command to see
     * whether we really want to stackBack.
     * 
     * @param command The command to be processed
     */
    private void stackBack(Command command) 
    {
        if(command.hasSecondWord()) {
            System.out.println("StackBack what?");
        }
        else {
            // step back one room in our stack of rooms history, if possible
            if (previousRoomStack.isEmpty()) {
                System.out.println("No room to go stack back to.");
            } else {
                // current room becomes previous room, and
                // current room is taken from the top of the stack
                previousRoom = currentRoom;
                currentRoom = previousRoomStack.pop();
                // and print description
                System.out.println(printRoomAndCarry());
            }
        }
    }
    
    /**
     * take, takes the item from the room by removeing it from list, saves it 
     * to the item being held field and reduces the number of item can be held.
     * if the item is not in the room or the player is already holding something
     * tehn it prints so and doesn't change anything.
     * At the begining of the game, the player must eat the cookie to gain strength
     * 
     * @param command The command to be processed
     */
    private void take(Command command)
    {
        if(command.hasSecondWord()) 
        {
            if (numberHeld > 0 || command.getSecondWord().equals("cookie"))
            {
                if (itemHeld != null)
                {
                    System.out.println("You are already holding something");
                }
                else if (currentRoom.itemInRoom(command.getSecondWord()) && itemHeld == null)
                {
                    itemHeld = currentRoom.removeItem(command.getSecondWord());
                    if (!itemHeld.getName().equals("cookie"))
                    {
                        numberHeld--;
                    }
                    System.out.println("You picked up "+ command.getSecondWord());
                }
                else
                {
                    System.out.println("That item is not in the room :(");
                }
            }
            else
            {
                System.out.println("You are tired and hungary, go find and eat a cookies");
            }
        }
        else {
            System.out.println("take what?");
        }
        
    }
    
    /**
     * drop, drops the item held ny the player. If the player isn't holding anything
     * then it prints a message saying so.
     * When the item is dropped, the item gets added to the current room's list of
     * items.
     * 
     * @param command The command to be processed
     */
    private void drop(Command command)
    {
        if(command.hasSecondWord()) 
        {
            System.out.println("drop what?");
        }
        else {
            if (itemHeld != null)
            {
                System.out.println("You have dropped "+ itemHeld.getName());
                currentRoom.addItem(itemHeld);
                itemHeld = null;
            }
            else
            {
                System.out.println("You have nothing to drop");
            }
            
        }
    }
    
    /**
     * printRoomAndCarry is a method that returns a string message that includes
     * the long description of the current room and the items in it and the item
     * held by the player.
     * 
     * @return String long description of the current room and the item held by player
     */
    private String printRoomAndCarry()
    {
        if (itemHeld != null)
        {
            return currentRoom.getLongDescription() + "\nYou are holding: "+ itemHeld.getName();
        }
        return currentRoom.getLongDescription() + "\nYou are holding nothing";
    }
    
    /**
     * charge, is a method that charges the beamer. The method first checks if the
     * item held by the player is a beamer, if so it charge it and print a message
     * saying so. If teh beamer is already charged then it doesn't do anything and
     * print the message saying so.
     * 
     * @param command The command to be processed
     */
    private void charge(Command command)
    {
        if(command.hasSecondWord()) 
        {
            System.out.println("charge what?");
        }
        else
        {
            if (itemHeld == null)
            {
                System.out.println("You are not holding a beamer");
            }
            else if (itemHeld.getName().equals("beamer"))
            {
                if (((Beamer)itemHeld).isCharged() == false)
                {
                    ((Beamer)itemHeld).charge(currentRoom);
                    System.out.println("beamer successfully charged");
                }
                else
                {
                    System.out.println("beamer already charged");
                }
            }
        }
    }
    
    /**
     * fire, is a method that fires the beamer. The player must hold the beamer item
     * and the beamer must be charged before firing. If the the beamer isn't charged or
     * isn't in the players hand, then it doesn't anything and print a message saying so.
     * 
     * @param command The command to be processed
     */
    private void fire(Command command)
    {
        if(command.hasSecondWord()) 
        {
            System.out.println("fire what?");
        }
        else
        {
            if (itemHeld == null)
            {
                System.out.println("You are not holding a beamer");
            }
            else if (itemHeld.getName().equals("beamer"))
            {
                if (((Beamer)itemHeld).isCharged())
                {
                    currentRoom = ((Beamer)itemHeld).fire();
                    System.out.println("beamer successfully fired");
                    look(command);
                }
                else
                {
                    System.out.println("beamer is not charged");
                }
            }
        }
    }
}
