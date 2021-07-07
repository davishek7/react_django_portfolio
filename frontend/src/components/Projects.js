import React,{useState,useEffect} from 'react'
import axios from 'axios'
import Project from './Project'

const Projects = () => {

    const [projects,setProjects] = useState([])

    useEffect(()=>{ 
        const getDataFromAPI = async () =>{
            const res = await axios.get('/api/')
            setProjects(res.data)
        }
        getDataFromAPI();
    },[])

    return (
        <section className="s1">
            <div className="main-container">
                <h3 style={{textAlign: "center"}}>Some of my past projects</h3>
                <div className="post-wrapper">
                {
                    projects.map((project,index)=>(
                        <Project project={project} key={index}/>
                    ))
                }
                </div>
            </div>
      </section>
    )
}

export default Projects
