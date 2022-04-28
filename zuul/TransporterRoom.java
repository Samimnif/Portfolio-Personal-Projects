import java.util.Random;
import java.util.ArrayList;

/**
 * TransporterRoom is a subclass of Room.
 * This class represents a transport room which will transport the player to a 
 * random room in the game of Zuul.
 * 
 * The transport object used Room constructor. It generates random number that
 * associated to rooms in the list.
 * The player then exits transport room and goes to the random selected room.
 *
 * @author Sami Mnif (101199669)
 * @version 2022.03.19
 */
public class TransporterRoom extends Room
{
    // array list from Room's static list
    ArrayList<Room> rooms;
    // random number generator
    Random rand;
    /**
     * Constructor for objects of class TransporterRoom
     * Uses Room's constructor to intialize room.
     * Intializes array and random
     */
    public TransporterRoom()
    {
        super("in a transporter room..");
        rand = new Random();
        rooms = getRooms();
    }
    
    /**
    * Returns a random room, independent of the direction parameter.
    * Gets the random selected room from findRandomRoom() method.
    * Overrides the original method.
    *
    * @param direction Ignored.
    * @return A randomly selected room.
    */
    public Room getExit(String direction)
    {
        return findRandomRoom();
    }
    
    /**
    * Choose a random room and returns it.
    *
    * @return The room we end up in upon leaving this one.
    */
    private Room findRandomRoom()
    {
        int roomNum = rand.nextInt(rooms.size());
        return rooms.get(roomNum);
    }
}