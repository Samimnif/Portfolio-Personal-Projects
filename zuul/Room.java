import java.util.Set;
import java.util.HashMap;
import java.util.Iterator;
import java.util.ArrayList; // or java.util.*; and replace the above

/**
 * Assignment 4
 * Used the provided sample solution to assignment 3.
 * 
 * Class Room - a room in an adventure game.
 *
 * This class is part of the "World of Zuul" application. 
 * "World of Zuul" is a very simple, text based adventure game.  
 *
 * A "Room" represents one location in the scenery of the game.  It is 
 * connected to other rooms via exits.  For each existing exit, the room 
 * stores a reference to the neighboring room.
 * Each room has a list of items in it.
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

public class Room 
{
    private String description;
    private HashMap<String, Room> exits;        // stores exits of this room.

    // the items in this room
    private ArrayList<Item> items;
    // static ArrayList of Rooms initialized
    private static ArrayList<Room> rooms = new ArrayList<Room>();
    
    /**
     * Create a room described "description". Initially, it has
     * no exits. "description" is something like "a kitchen" or
     * "an open court yard".
     * Adds the room to the static ArrayList rooms field for later use.
     * 
     * @param description The room's description.
     */
    public Room(String description) 
    {
        this.description = description;
        exits = new HashMap<String, Room>();
        items = new ArrayList<Item>();
        rooms.add(this);
    }
    
    /**
     * Add an item to the room, best to check that it's not null.
     * 
     * @param item The item to add to the room
     */
    public void addItem(Item item) 
    {
        if (item!=null) { // not required, but good practice
            items.add(item);
        }
    }

    /**
     * Define an exit from this room.
     * 
     * @param direction The direction of the exit
     * @param neighbour The room to which the exit leads
     */
    public void setExit(String direction, Room neighbour) 
    {
        exits.put(direction, neighbour);
    }

    /**
     * Returns a short description of the room, i.e. the one that
     * was defined in the constructor
     * 
     * @return The short description of the room
     */
    public String getShortDescription()
    {
        return description;
    }

    /**
     * Return a long description of the room in the form:
     *     You are in the kitchen.
     *     Exits: north west
     *     Items: 
     *        a chair weighing 5 kgs.
     *        a table weighing 10 kgs.
     *     
     * @return A long description of this room
     */
    public String getLongDescription()
    {
        return "You are " + description + ".\n" + getExitString()
            + "\nItems:" + getItems();
    }

    /**
     * Return a string describing the room's exits, for example
     * "Exits: north west".
     * 
     * @return Details of the room's exits
     */
    private String getExitString()
    {
        String returnString = "Exits:";
        Set<String> keys = exits.keySet();
        for(String exit : keys) {
            returnString += " " + exit;
        }
        return returnString;
    }

    /**
     * Return the room that is reached if we go from this room in direction
     * "direction". If there is no room in that direction, return null.
     * 
     * @param direction The exit's direction
     * @return The room in the given direction
     */
    public Room getExit(String direction) 
    {
        return exits.get(direction);
    }
    
    /**
     * Return a String representing the items in the room, one per line.
     * 
     * @return A String of the items, one per line
     */
    public String getItems() 
    {
        // let's use a StringBuilder (not required)
        StringBuilder s = new StringBuilder();
        for (Item i : items) {
            s.append("\n    " + i.getDescription());
        }
        return s.toString(); 
    }
    
    /**
     * removeItem is a method that removes the specified item from ArrayList 
     * items and returns that removed item.
     * 
     * @param itemName String containing the name of the item
     * @return Item the removed item from the ArrayList
     */
    public Item removeItem(String itemName)
    {
        if (itemName!=null) { // not required, but good practice
            Iterator<Item> itr = items.iterator();
            Item tempSave = null;
            while (itr.hasNext())
            {
                Item curr = itr.next();
                if (curr.getName().equals(itemName))
                {
                    tempSave = curr;
                    itr.remove();
                    return tempSave;
                }
                
            }
            
        }
        return null;
    }
    
    /**
     * itemInRoom is a method that checks if the item is in the room.
     * returns true if the item was found in the list, false otherwise
     * 
     * @param String itemName the name of the item.
     * @return boolean true if the item is in the room, false otherwise.
     */
    public boolean itemInRoom(String itemName)
    {
        if (itemName!=null) { // not required, but good practice
            Iterator<Item> itr = items.iterator();
            while (itr.hasNext())
            {
                Item curr = itr.next();
                if (curr.getName().equals(itemName))
                {
                    return true;
                }
                
            }
            
        }
        return false;
    }
    
    /**
     * getRooms is a static method that returns the list of rooms added to the
     * static ArryList rooms.
     * 
     * @return ArrayList rooms that contains all rooms added in the game.
     */
    public static ArrayList getRooms()
    {
        return rooms;
    }
}

