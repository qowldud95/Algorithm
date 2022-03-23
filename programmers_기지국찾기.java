class Solution {
    public int solution(int n, int[] stations, int w) {
        //최소 기지국의 갯수
        int answer = 0;

        //전파 못받는 범위 
        int notSpread = 0;

        //전파 시작 범위
        int notSpreadStartIndex = 1;

        for(int i=0; i < stations.length; i++){
            if(notSpreadStartIndex < stations[i] - w){
                notSpread = stations[i] - w - notSpreadStartIndex;

                //범위에 따른 최소기지국 개수
                int count = notSpread / (w*2+1);
                if(notSpread % (w*2+1) !=0){
                    count++;
                }
                answer += count;     
            }
            notSpreadStartIndex = stations[i] + w + 1;
        }
        if(stations[stations.length-1] + w + 1 <= n) {
            notSpreadStartIndex = stations[stations.length-1] + w + 1;
            notSpread = n + 1 - notSpreadStartIndex;

            int count = notSpread/(w * 2 + 1);
            if(notSpread % (w * 2 + 1) != 0){
                count++;
            }
            answer += count;
        }

        return answer;
    }
}