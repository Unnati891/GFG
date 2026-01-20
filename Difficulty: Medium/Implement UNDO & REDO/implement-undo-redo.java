class Solution {
    Stack<Character>ok=new Stack<>();
    Stack<Character>Notok=new Stack<>();
    public void append(char x) {
        // append x into document
        ok.push(x);
        Notok.clear();
        
    }
    public void undo() {
        // undo last change
        if(!ok.isEmpty()){
            Notok.push(ok.pop());
        }
    }

    public void redo() {
        // redo changes
        if(!Notok.isEmpty()){
            ok.push(Notok.pop());
        }
    }

    public String read() {
        // read the document
        StringBuilder sb=new StringBuilder();
        for(int i=0;i<ok.size();i++){
            sb.append(ok.get(i));
        }
        return sb.toString();
    }
}
