struct ContentView: View {
    @State var showView = false
    var body: some View {
        NavigationView {
            VStack {
                Button(action: {
                    print("*** Login in progress... ***")
                    DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
                        self.showView = true
                    }
                }) {
                    Text("Push me and go on")
                }

                //MARK: - NAVIGATION LINKS
                NavigationLink(destination: PushedView(), isActive: $showView) {
                    EmptyView()
                }
            }
        }
    }
}


struct PushedView: View {
    var body: some View {
        Text("This is your pushed view...")
            .font(.largeTitle)
            .fontWeight(.heavy)
    }
}