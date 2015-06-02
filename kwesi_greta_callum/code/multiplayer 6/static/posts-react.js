/** @jsx React.DOM */

var Posts = React.createClass({
    getInitialState: function() {
        return {
            posts: []
        };
    },

    loadPostsFromServer: function() {
        $.ajax({type: "GET",
            url: "http://localhost:8080/posts",
            dataType: 'json',
            success: function(result) {
                if (this.isMounted()) {
                    this.setState({posts: result});
                }
            }.bind(this)
        });
    },

    componentDidMount: function() {
        this.loadPostsFromServer();
        setInterval(this.loadPostsFromServer, 2000)
    },

    render: function() {

        return <div>
            {this.state.posts.map(function (p) {
                return <div>{p.sentence}</div>
            })}
        </div>;
    }
});

React.renderComponent(
    <Posts />,
    document.getElementById("posts")
);
