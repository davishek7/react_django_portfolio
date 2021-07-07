import React from 'react'
import { FaGithub,FaExternalLinkAlt } from 'react-icons/fa';

const Project = ({project}) => {
    return (
        <div>
        <div className="post">
            <img src={project.image} className="thumbnail" alt={project.title}/>
            <div className="post-preview">
                <h6 className="post-title">{project.title}</h6>
                <div style={{padding:"20px"}}>
                    <a href={project.github_repo} target="_blank" rel="noreferrer" style={{fontSize: "25px", float:"left",color:"black"}}><FaGithub/></a>
                    <a target="_blank" rel="noreferrer" href={project.live_url} style={{float:"right"}}><FaExternalLinkAlt/></a>
                </div>
            </div>
        </div>
    </div>
    )
}

export default Project
