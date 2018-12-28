from sklearn.tree import export_graphviz
    export_graphviz(
            tree_clf,
            out_file=image_path("iris_tree.dot"),
            feature_names=iris.feature_names[2:],
            class_names=iris.target_names,
            rounded=True,
            filled=True
        )