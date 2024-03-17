import org.junit.Test;
import static org.junit.Assert.*;

public class RearangeArrayEllementsBySignTest {
    
    @Test
    public void testRearrangeArray() {
        RearangeArrayEllementsBySign rearranger = new RearangeArrayEllementsBySign();
        
        // Test case 1: Positive and negative numbers
        int[] nums1 = {1, -2, 3, -4, 5};
        int[] expected1 = {1, -2, 3, -4, 5};
        assertArrayEquals(expected1, rearranger.rearrangeArray(nums1));
        
        // Test case 2: Only positive numbers
        int[] nums2 = {1, 2, 3, 4, 5};
        int[] expected2 = {1, 2, 3, 4, 5};
        assertArrayEquals(expected2, rearranger.rearrangeArray(nums2));
        
        // Test case 3: Only negative numbers
        int[] nums3 = {-1, -2, -3, -4, -5};
        int[] expected3 = {-1, -2, -3, -4, -5};
        assertArrayEquals(expected3, rearranger.rearrangeArray(nums3));
        
        // Test case 4: Empty array
        int[] nums4 = {};
        int[] expected4 = {};
        assertArrayEquals(expected4, rearranger.rearrangeArray(nums4));
    }
}