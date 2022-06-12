import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> hash = new HashMap<>();
        int answer = 1;
        
        for(int i=0; i<clothes.length; i++){
            hash.put(clothes[i][1], hash.getOrDefault( clothes[i][1], 0) + 1);
        }
        for(String key : hash.keySet()){
            answer  *= (hash.get(key) + 1);
        }
        answer -= 1;
        return answer;
    }
}