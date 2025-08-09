// https://leetcode.com/problems/contains-duplicate/submissions/1728711397/
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> sets=new HashSet<>();
        for(int i:nums){
            sets.add(i);
        }
        if(nums.length==sets.size()){
            return false;
        }
        return true;
    }
}