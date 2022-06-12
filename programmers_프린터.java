import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        //문서의 중요도가 순서대로 담긴 배열을 우선순위 큐에 내림차순으로 넣는다.
        //우선순위큐 pq에서 꺼낸값(pq.peek())이 priorities배열길이만큼 for문을 돌면서
        // 값이 같을 때 i값을 찾고, 그 값이 location과 같을 때, 인쇄순서 answer를 출력
        //내가 인쇄를 요청한 문서가 몇번째로 인쇄되는지 answer에 넣는다.
        
        int answer = 1;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
         
        for(int n : priorities){
            pq.offer(n);    
        } 
       
        while(!pq.isEmpty()){
            for(int i=0; i<priorities.length; i++){
                if(pq.peek() == priorities[i]){
                    if(location == i){
                        return answer;
                    }
                pq.poll();
                answer++;
                }
            }
        }
        
        return answer;
    }
}