import React from "react";
import { history } from "../../history";

export function Home() {
    return (
        <div className={"homeWrapper"}>
            <p className={"heading"}>Designed by Alfred Joel</p>
            <div className="topicWrapper">
                <h1 className={"topic"}>Inventory Management</h1>
                <h1 className={"topic2"}>System</h1>
            </div>
            <div className={"productsWrapper"}>
                <div className={"productsChildWrapper"} onClick={() => {
                    history.push("/add")
                }}>
                    <p>Add</p>
                    <span>Products / Location</span>
                </div>
                <div className={"productsChildWrapper"} onClick={() => {
                    history.push("/view")
                }}>
                    <p>View</p>
                    <span>Products / Location</span>
                </div>
                <div className={"productsChildWrapper"} onClick={() => {
                    history.push("/edit")
                }}>
                    <p>Edit</p>
                    <span>Products / Location</span>
                </div>
            </div>
        </div>
    );
};
