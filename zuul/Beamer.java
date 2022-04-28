/**
 * Beamer is a subclass of Item.
 * This class represents a beamer item which may be put
 * in a room in the game of Zuul.
 * 
 * A beamer can charge and fire. When charged the beamer saves the room where
 * it was chraged and whenever the player fires it, the beamer teleports him
 * back to the saved room.
 *
 * @author Sami Mnif (101199669)
 * @version 2022.03.19
 */
public class Beamer extends Item
{
    // boolean shows if the beamer is chraged or not (true or false)
    private boolean charged;
    // the room where the beamer was charged
    private Room saveRoom;
    /**
     * Constructor for objects of class Beamer.
     * Created Beamer item using the Item constructor and sets charge 
     * as false and saveRoom as null by default
     */
    public Beamer()
    {
        super("beamer", "magical beamer", 2);
        this.charged = false;
        this.saveRoom = null;
    }

    /**
     * isCharged is a method that returns a boolean indicating if the beamer is
     * charged or not (true or false).
     * 
     * @return charged boolean, true if the beamer is charged, false otherwise.
     */
    public boolean isCharged()
    {
        return charged;
    }
    
    /**
     * charge is a method that charges the beamer by setting the charge field
     * as true and saves the current room to the saveRoom field.
     * 
     * @param currenRoom Room object represents room where the beamer is charged
     */
    public void charge(Room currentRoom)
    {
        charged = true;
        saveRoom = currentRoom;
    }
    
    /**
     * fire method fires the beamer by setting the charge field back to false
     * and returning the previously saved room in saveRoom field.
     * Returns null if the beamer wasn't charged.
     * 
     * @return saveRoom the room where the beamer was charged, return null if wasn't successful
     */
    public Room fire()
    {
        if (charged == true)
        {
            charged = false;
            return saveRoom;
        }
        return null;
    }
}
