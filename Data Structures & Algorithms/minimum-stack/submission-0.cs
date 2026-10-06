public class MinStack {
    private List<int> obj;
    public MinStack() {
        obj = [];
    }
    
    public void Push(int val) {
        obj.Add(val);
    }
    
    public void Pop() {
        obj.RemoveAt(obj.Count - 1);
    }
    
    public int Top() {
        return obj[^1];
    }
    
    public int GetMin() {
        int minLength = obj[0];
        foreach (int i in obj)
        {
            if (minLength > i)
            {
                minLength = i;
            }
        }
        return minLength;
    }
}
